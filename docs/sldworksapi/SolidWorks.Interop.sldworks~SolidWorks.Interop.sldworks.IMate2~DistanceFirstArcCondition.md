# DistanceFirstArcCondition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceFirstArcCondition`

Gets the the first arc condition of this distance mate between cylindrical components.
Gets the the first arc condition of this distance mate between cylindrical components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DistanceFirstArcCondition As System.Integer
```

```

Dim instance As IMate2
Dim value As System.Integer
 
value = instance.DistanceFirstArcCondition
```

```

System.int DistanceFirstArcCondition {get;}
```

```

property System.int DistanceFirstArcCondition {
   System.int get();
}
```

#### Property Value

Arc condition as defined by [swDistanceMateArcConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDistanceMateArcConditions_e.html)

Remarks

This property is valid only for distance mates between:

- two cylindrical faces

   - or -

- one cylindrical face and one axis.

Example

[Add and Edit Distance Mate (VBA)](Add_and_Edit_Distance_Mate_Example_VB.htm)  
[Add and Edit Distance Mate (VB.NET)](Add_and_Edit_Distance_Mate_Example_VBNET.htm)  
[Add and Edit Distance Mate (C#)](Add_and_Edit_Distance_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::DistanceSecondArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceSecondArcCondition.md)  
[IAssemblyDoc::AddDistanceMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.md)  
[IAssemblyDoc::EditDistanceMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditDistanceMate.md)
