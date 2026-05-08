# ExtrusionDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ExtrusionDirection`

Gets or sets the direction in which to extrude the rib.
Gets or sets the direction in which to extrude the rib.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExtrusionDirection As System.Integer
```

```

Dim instance As IRibFeatureData2
Dim value As System.Integer
 
instance.ExtrusionDirection = value
 
value = instance.ExtrusionDirection
```

```

System.int ExtrusionDirection {get; set;}
```

```

property System.int ExtrusionDirection {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Direction as defined in [swRibExtrusionDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRibExtrusionDirection_e.html)

Example

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)
