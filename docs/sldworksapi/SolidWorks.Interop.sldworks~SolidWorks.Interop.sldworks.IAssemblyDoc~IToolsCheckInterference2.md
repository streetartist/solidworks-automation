# IToolsCheckInterference2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference2`

Obsolete. See IAssemblyDoc::IToolsCheckInterference3.
Obsolete. See [IAssemblyDoc::IToolsCheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IToolsCheckInterference2( _
   ByVal NumComponents As System.Integer, _
   ByRef LpComponents As Component, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
) 
```

```

Dim instance As IAssemblyDoc
Dim NumComponents As System.Integer
Dim LpComponents As Component
Dim CoincidentInterference As System.Boolean
Dim PComp As System.Object
Dim PFace As System.Object
 
instance.IToolsCheckInterference2(NumComponents, LpComponents, CoincidentInterference, PComp, PFace)
```

```

void IToolsCheckInterference2( 
   System.int NumComponents,
   ref Component LpComponents,
   System.bool CoincidentInterference,
   out System.object PComp,
   out System.object PFace
)
```

```

void IToolsCheckInterference2( 
   System.int NumComponents,
   Component^% LpComponents,
   System.bool CoincidentInterference,
   [Out] System.Object^ PComp,
   [Out] System.Object^ PFace
) 
```

#### Parameters

*NumComponents*

*LpComponents*

*CoincidentInterference*

*PComp*

*PFace*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
