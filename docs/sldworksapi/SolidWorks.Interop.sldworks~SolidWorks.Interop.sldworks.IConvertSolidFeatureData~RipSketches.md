# RipSketches Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~RipSketches`

Gets or sets the sketches to use to define required rips in this convert solid feature.
Gets or sets the sketches to use to define required rips in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RipSketches As System.Object
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Object
 
instance.RipSketches = value
 
value = instance.RipSketches
```

```

System.object RipSketches {get; set;}
```

```

property System.Object^ RipSketches {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of rip [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)es

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)
