# FilletGussetEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletGussetEdges`

Gets or sets whether to fillet the edges of this gusset.
Gets or sets whether to fillet the edges of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FilletGussetEdges As System.Boolean
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Boolean
 
instance.FilletGussetEdges = value
 
value = instance.FilletGussetEdges
```

```

System.bool FilletGussetEdges {get; set;}
```

```

property System.bool FilletGussetEdges {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to fillet the edges of this gusset, false to not

Remarks

This property is valid only if [ISMGussetFeatureData::GussetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~GussetType.md) is set to 1.

After setting this property, set [ISMGussetFeatureData::EdgeFilletRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~EdgeFilletRadius.md).

Example

See the examples for [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)
