# DirectionPull Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~DirectionPull`

Gets or sets the direction in which to pull this draft feature.
Gets or sets the direction in which to pull this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DirectionPull As System.Object
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Object
 
instance.DirectionPull = value
 
value = instance.DirectionPull
```

```

System.object DirectionPull {get; set;}
```

```

property System.Object^ DirectionPull {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Face from which to pull this draft feature

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)
