# Segments Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~Segments`

Gets and sets the sketch segments to use in this structural-member group.
Gets and sets the sketch segments to use in this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Segments As System.Object
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Object
 
instance.Segments = value
 
value = instance.Segments
```

```

System.object Segments {get; set;}
```

```

property System.Object^ Segments {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)

Example

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)  
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)  
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)  
[Create Structural-Member Group (VBA)](Create_Structural_Member_Group_Example_VB.htm)  
[Create Structural-Member Group (VB.NET)](Create_Structural_Member_Group_Example_VBNET.htm)  
[Create Structural-Member Group (C#)](Create_Structural_Member_Group_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)  
[IStructuralMemberGroup::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~IGetSegments.md)  
[IStructuralMemberGroup::ISetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ISetSegments.md)
