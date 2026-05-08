# GetSelectionSpecification Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification`

Gets the selection specification at the specified index of the current selection list.
Gets the selection specification at the specified index of the current selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionSpecification( _
   ByVal Index As System.Integer, _
   ByRef SelectByString As System.String, _
   ByRef ObjectType As System.String, _
   ByRef Type As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

```

Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim SelectByString As System.String
Dim ObjectType As System.String
Dim Type As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.GetSelectionSpecification(Index, SelectByString, ObjectType, Type, X, Y, Z)
```

```

System.bool GetSelectionSpecification( 
   System.int Index,
   out System.string SelectByString,
   out System.string ObjectType,
   out System.int Type,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

```

System.bool GetSelectionSpecification( 
   System.int Index,
   [Out] System.String^ SelectByString,
   [Out] System.String^ ObjectType,
   [Out] System.int Type,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
) 
```

#### Parameters

*Index*
:   1 <= Index in the current list of selected items <= [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md)

*SelectByString*
:   Feature name of object at Index; "" if object is not a feature

*ObjectType*
:   Type of object at Index

*Type*
:   Type of object at Index as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*X*
:   X coordinate of object at Index; 0 if SelectByString is not ""

*Y*
:   Y coordinate of object at Index; 0 if SelectByString is not ""

*Z*
:   Z coordinate of object at Index; 0 if SelectByString is not ""

#### Return Value

True if successful, false if not

Example

[Get Selection Specification (VBA)](Get_Selection_Specification_Example_VB.htm)  
[Get Selection Specification (VB.NET)](Get_Selection_Specification_Example_VBNET.htm)  
[Get Selection Specification (C#)](Get_Selection_Specification_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::GetSelectByIdSpecification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.md)  
[ISelectionMgr::GetSelectedObject6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)  
[IModelDocExtension::SelectByID2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)  
[IFeature::GetNameForSelection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.md)  
[ISelectionMgr::GetSelectedObjectLoop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md)  
[ISelectionMgr::GetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md)  
[ISelectionMgr::GetSelectedObjectsComponent4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.md)  
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md)  
[ISelectionMgr::GetSelectedObjectType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md)  
[ISelectionMgr::GetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.md)  
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::SetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectedObjectMark.md)  
[ISelectionMgr::SetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.md)
