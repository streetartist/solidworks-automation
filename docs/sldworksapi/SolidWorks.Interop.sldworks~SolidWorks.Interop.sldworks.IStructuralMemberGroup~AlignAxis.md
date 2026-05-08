# AlignAxis Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~AlignAxis`

Gets and sets the axis on which to align this structural-member group.
Gets and sets the axis on which to align this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AlignAxis As System.Integer
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Integer
 
instance.AlignAxis = value
 
value = instance.AlignAxis
```

```

System.int AlignAxis {get; set;}
```

```

property System.int AlignAxis {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Axis as defined in [swMirrorProfileOrAlignmentAxis\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorProfileOrAlignmentAxis_e.html)

Example

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)  
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)  
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)
