# Direction Property (IDomeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Direction`

Gets or sets the direction of the dome feature.
Gets or sets the direction of the dome feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Direction As System.Object
```

```

Dim instance As IDomeFeatureData2
Dim value As System.Object
 
instance.Direction = value
 
value = instance.Direction
```

```

System.object Direction {get; set;}
```

```

property System.Object^ Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Edge indicating the direction of dome feature

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get and Set Direction for Dome Feature (VBA)](Get_and_Set_Direction_for_Dome_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md)  
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.md)
