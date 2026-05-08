# IToolsCheckInterference3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3`

Obsolete.
Obsolete.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IToolsCheckInterference3( _
   ByVal NumComponents As System.Integer, _
   ByRef LpComponents As Component2, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
) 
```

```

Dim instance As IAssemblyDoc
Dim NumComponents As System.Integer
Dim LpComponents As Component2
Dim CoincidentInterference As System.Boolean
Dim PComp As System.Object
Dim PFace As System.Object
 
instance.IToolsCheckInterference3(NumComponents, LpComponents, CoincidentInterference, PComp, PFace)
```

```

void IToolsCheckInterference3( 
   System.int NumComponents,
   ref Component2 LpComponents,
   System.bool CoincidentInterference,
   out System.object PComp,
   out System.object PFace
)
```

```

void IToolsCheckInterference3( 
   System.int NumComponents,
   Component2^% LpComponents,
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
:   True to check for coincident interference, false to not

*PComp*
:   Array of components where interference has been found

*PFace*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) where interference has been found

Remarks

This method returns:

- an empty array of faces for components that have coincident faces that touch.
- an array of components for components that touch.

For each face that intersects, there is a corresponding component.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.md)  
[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.md)  
[IModeler::CheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.md)  
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md)  
[IModeler::ICheckInterferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.md)
