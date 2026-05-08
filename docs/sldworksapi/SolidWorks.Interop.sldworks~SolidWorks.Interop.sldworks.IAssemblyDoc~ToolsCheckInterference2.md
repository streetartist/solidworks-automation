# ToolsCheckInterference2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2`

Checks for interference between parts in this assembly.
Checks for interference between parts in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ToolsCheckInterference2( _
   ByVal NumComponents As System.Integer, _
   ByVal LpComponents As System.Object, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
) 
```

```

Dim instance As IAssemblyDoc
Dim NumComponents As System.Integer
Dim LpComponents As System.Object
Dim CoincidentInterference As System.Boolean
Dim PComp As System.Object
Dim PFace As System.Object
 
instance.ToolsCheckInterference2(NumComponents, LpComponents, CoincidentInterference, PComp, PFace)
```

```

void ToolsCheckInterference2( 
   System.int NumComponents,
   System.object LpComponents,
   System.bool CoincidentInterference,
   out System.object PComp,
   out System.object PFace
)
```

```

void ToolsCheckInterference2( 
   System.int NumComponents,
   System.Object^ LpComponents,
   System.bool CoincidentInterference,
   [Out] System.Object^ PComp,
   [Out] System.Object^ PFace
) 
```

#### Parameters

*NumComponents*
:   Number of components to check

*LpComponents*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) being checked for interference

*CoincidentInterference*
:   True to treat coincident entities as interference, false to not

*PComp*
:   Array of components where interferences have been found

*PFace*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) where interferences have been found

Remarks

This method returns:

- an empty array of faces for components that have coincident faces that touch.
- an array of components for components that touch.

For each face that intersects, there is a corresponding component.

**NOTE:** The obsolete method, IAssemblyDoc::ToolsCheckInterference, displays the Interference Detection PropertyManager, but this method does not.

Example

[Check Interference (VBA)](Check_Interference_using_AssemblyDoc_ToolsCheckInterference2_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md)  
[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.md)  
[IModeler::ICheckInterferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.md)  
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md)  
[IModeler::CheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.md)
