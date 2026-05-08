# PickPoints Property (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~PickPoints`

Gets or sets the pick points of a loft feature.
Gets or sets the pick points of a loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PickPoints As System.Object
```

```

Dim instance As ILoftFeatureData
Dim value As System.Object
 
instance.PickPoints = value
 
value = instance.PickPoints
```

```

System.object PickPoints {get; set;}
```

```

property System.Object^ PickPoints {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of the pick points that contain arrays of coordinates of the pick points of this loft feature

Example

[Get and Set Loft's Pick Points (VB.NET)](Get_Loft's_Pick_Points_Example_VBNET.htm)  
[Get and Set Loft's Pick Points (C#)](Get_Loft's_Pick_Points_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)
