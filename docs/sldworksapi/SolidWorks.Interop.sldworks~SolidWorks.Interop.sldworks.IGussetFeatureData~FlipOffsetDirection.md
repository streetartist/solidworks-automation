# FlipOffsetDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~FlipOffsetDirection`

Gets or sets whether the offset direction is flipped for this gusset feature.
Gets or sets whether the offset direction is flipped for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipOffsetDirection As System.Boolean
```

```

Dim instance As IGussetFeatureData
Dim value As System.Boolean
 
instance.FlipOffsetDirection = value
 
value = instance.FlipOffsetDirection
```

```

System.bool FlipOffsetDirection {get; set;}
```

```

property System.bool FlipOffsetDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the offset direction, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)
