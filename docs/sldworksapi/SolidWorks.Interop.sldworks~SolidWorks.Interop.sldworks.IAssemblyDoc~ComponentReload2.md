# ComponentReload2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ComponentReload2`

Reloads and/or sets the read-only state of the specified component.
Reloads and/or sets the read-only state of the specified component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ComponentReload2( _
   ByVal Component As System.Object, _
   ByVal ReadOnly As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim Component As System.Object
Dim ReadOnly As System.Boolean
Dim Options As System.Integer
Dim value As System.Integer
 
value = instance.ComponentReload2(Component, ReadOnly, Options)
```

```

System.int ComponentReload2( 
   System.object Component,
   System.bool ReadOnly,
   System.int Options
)
```

```

System.int ComponentReload2( 
   System.Object^ Component,
   System.bool ReadOnly,
   System.int Options
) 
```

#### Parameters

*Component*
:   [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

*ReadOnly*
:   True to set Component read-only after reload, false to allow write access

*Options*
:   Reload option as defined by [swComponentReloadOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentReloadOption_e.html)

#### Return Value

Error code as defined by [swComponentReloadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentReloadError_e.html)

Remarks

This method is analogous to the Reload dialog that appears when you right-click on an assembly component in the FeatureManager design tree and select **Reload**. For more information, read the **SOLIDWORKS user-interface Help > Fundamentals > Document Basics > Multi-User Environment > Reload** topic.

Example

'VBA

'Preconditions:

'1. Open *public\_documents***\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\api\arm2.sldasm**.

'2. Open the Immediate window.

'Postconditions:

' Inspect the Immediate window.

'=============================================

Dim swApp As SldWorks.SldWorks  
Dim SWMODEL As SldWorks.ModelDoc2  
Dim SWASSY As SldWorks.AssemblyDoc  
Dim swcomponent As SldWorks.Component2  
Dim Error As swComponentReloadError\_e  
Option Explicit  
Sub main()  
    Set swApp = Application.SldWorks  
    Set SWMODEL = swApp.ActiveDoc  
    Set SWASSY = SWMODEL  
    Set swcomponent = SWASSY.GetComponentByName("secondgrip-1")  
    Debug.Print swcomponent.GetPathName  
    Error = SWASSY.**ComponentReload2**(swcomponent, True, swComponentReloadOption\_e.swDontReloadOldComponents)  
    Debug.Print "Error code: " & Error  
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ReplaceComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents2.md)  
[IModelDoc2::ReloadOrReplace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace.md)
