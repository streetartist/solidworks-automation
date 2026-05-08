# ICoordinateSystemElement Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement`

Allows access to a coordinate system element.
Allows access to a coordinate system element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICoordinateSystemElement 
```

```

Dim instance As ICoordinateSystemElement
```

```

public interface ICoordinateSystemElement 
```

```

public interface class ICoordinateSystemElement 
```

Remarks

The normal channel of feature editing (IFeature::CreateDefinition, IFeature::ModifyDefinition) will not work for features created with coordinate system elements. In order to edit a feature created with a coordinate system element, you must:

1. Select the feature created with a coordinate system element.
2. Call the IModelDocExtension::RunCommand swCommands\_e.swCommands\_EditFeature to open a PropertyManager dialog for the selected object.
3. Call ISelectionMgr::GetSelectedObjectType3 to obtain the selection.
4. Test whether the selection is a coordinate system element.
5. If the selection is a coordinate system element, obtain the CoordinateSystemElement object.

'VBA

'---------------------------------------------------------------------  
' Preconditions:  
' 1. Open a part that contains an Axis1 created using a coordinate system element.  
' 2. Open the Immediate window.  
'  
' Postconditions:  
' 1. Examine the Immediate window to see the coordinate system element type as defined by swCoordSysElementType\_e.  
' 2. Examine the user interface. The specified coordinate system element should be selected.  
'  
'---------------------------------------------------------------------  
Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swSelMgr As SldWorks.SelectionMgr  
Dim iSelType As Long  
Dim isCoordSysElmSelected As Boolean  
Dim swCordSysElement As SldWorks.CoordinateSystemElement  
Dim boolstatus As Boolean

Sub main()

    Set swApp = Application.SldWorks  
     
    Set swModel = swApp.ActiveDoc  
    boolstatus = swModel.Extension.SelectByID2("Axis1", "AXIS", 0, 0, 0, False, 0, Nothing, 0)  
    swModel.Extension.RunCommand swCommands\_e.swCommands\_EditFeature, ""  
     
    Set swSelMgr = swModel.SelectionManager  
    iSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
     
    If iSelType = swSelCOORDSYS Then  
     
        isCoordSysElmSelected = swSelMgr.IsCoordSysElementSelected(1, -1)  
     
        If isCoordSysElmSelected Then  
     
            Set swCordSysElement = swSelMgr.GetSelectedCoordSysElement(1, -1)  
            Debug.Print "Element type: " & swCordSysElement.GetElementType  
                         
        End If  
     
    End If  
    swModel.Extension.RunCommand swCommands\_e.swCommands\_Dve\_Rmb\_Cancel, ""  
    Set swCordSysElement = Nothing

End Sub

Example

‘VBA

'---------------------------------------------------------------------

' Preconditions:

' 1. Open a part with a coordinate system.

' 2. Select any coordinate system element.

' 3. Open the Immediate window.

'

' Postconditions: Examine the Immediate window for the type of coordinate system element selected.

'---------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFeat As SldWorks.Feature

Dim swComponent As SldWorks.Component2

Dim swCoordSysFeat As SldWorks.CoordinateSystemFeatureData

Dim iSelType As Long

Dim isCoordSysElmSelected As Boolean

Dim swCordSysElement As SldWorks.CoordinateSystemElement

Dim boolstatus As Boolean

Sub main()

    Set swApp = Application.SldWorks

    Set swModel = swApp.ActiveDoc

    'boolstatus = swModel.Extension.SelectByID2("Coordinate System1\X Axis", "COORDSYS", 0, 0, 0, False, 0, Nothing, 0)

    'Select any coordinate system element

    'Stop

    Set swSelMgr = swModel.SelectionManager

    Set swComponent = swSelMgr.GetSelectedObjectsComponent4(1, -1)

    iSelType = swSelMgr.GetSelectedObjectType3(1, -1)

    If iSelType = swSelCOORDSYS Then

        isCoordSysElmSelected = swSelMgr.**IsCoordSysElementSelected**(1, -1)

        If isCoordSysElmSelected = True Then

            Set swCordSysElement = swSelMgr.**GetSelectedCoordSysElement**(1, -1)

            Dim ElementType As Long

            ElementType = swCordSysElement.**GetElementType**

            Debug.Print "ElementType: " & ElementType

            Set swFeat = swCordSysElement.**GetCoordinateSystem**

            Set swCoordSysFeat = swFeat.GetDefinition

            swCoordSysFeat.AccessSelections swModel, swComponent

            'Stop

            swCoordSysFeat.ReleaseSelectionAccess

        End If

    End If

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoordinateSystemElement Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
