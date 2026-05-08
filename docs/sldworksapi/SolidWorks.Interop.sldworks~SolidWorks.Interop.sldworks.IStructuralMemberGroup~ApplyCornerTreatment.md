# ApplyCornerTreatment Property (IStructuralMemberGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ApplyCornerTreatment`

Gets and sets whether or not to apply a corner treatment to this structural-member group.
Gets and sets whether or not to apply a corner treatment to this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ApplyCornerTreatment As System.Boolean
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Boolean
 
instance.ApplyCornerTreatment = value
 
value = instance.ApplyCornerTreatment
```

```

System.bool ApplyCornerTreatment {get; set;}
```

```

property System.bool ApplyCornerTreatment {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to apply corner treatment, false to not

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
[IStructuralMemberGroup::CornerTreatmentType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~CornerTreatmentType.md)  
[IStructuralMemberGroup::MiterMergeCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MiterMergeCondition.md)
