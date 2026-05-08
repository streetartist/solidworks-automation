# BendDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDirection`

Gets the direction of this bend.
Gets the direction of this bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property BendDirection As System.Integer
```

```

Dim instance As IOneBendFeatureData
Dim value As System.Integer
 
value = instance.BendDirection
```

```

System.int BendDirection {get;}
```

```

property System.int BendDirection {
   System.int get();
}
```

#### Property Value

Bend direction as defined in [swBendDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendDirection_e.html)

Example

[Get Direction of a Bend (VBA)](Get_Direction_of_a_Bend_Example_VB.htm)  
[Get Direction of a Bend (VB.NET)](Get_Direction_of_a_Bend_Example_VBNET.htm)  
[Get Direction of a Bend (C#)](Get_Direction_of_a_Bend_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)  
[IOneBendFeatureData::BendDown Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDown.md)
