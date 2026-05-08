# IndentWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~IndentWidth`

Gets or sets the indent width of this gusset.
Gets or sets the indent width of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IndentWidth As System.Double
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Double
 
instance.IndentWidth = value
 
value = instance.IndentWidth
```

```

System.double IndentWidth {get; set;}
```

```

property System.double IndentWidth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Indent width

Remarks

This property is valid only if [ISMGussetFeatureData::ProfileDimensionScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.md) is set to 0.

Example

See the examples for [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)
