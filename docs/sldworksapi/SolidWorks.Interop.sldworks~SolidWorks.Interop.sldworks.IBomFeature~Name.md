# Name Property (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Name`

Gets the name of this BOM table feature.
Gets the name of this BOM table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Name As System.String
```

```

Dim instance As IBomFeature
Dim value As System.String
 
instance.Name = value
 
value = instance.Name
```

```

System.string Name {get; set;}
```

```

property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of this BOM table feature

Example

[Export BOM's Second Column to BOM Table Area (C#)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_CSharp.htm)  
[Export BOM's Second Column to BOM Table Area (VB.NET)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VBNET.htm)  
[Export BOM's Second Column to BOM Table Area (VBA)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)
