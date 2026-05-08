# UseCentroid Property (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~UseCentroid`

Gets or sets whether to set the reference point to the centroid of the seed feature for this table-driven pattern feature.
Gets or sets whether to set the reference point to the centroid of the seed feature for this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseCentroid As System.Boolean
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Boolean
 
instance.UseCentroid = value
 
value = instance.UseCentroid
```

```

System.bool UseCentroid {get; set;}
```

```

property System.bool UseCentroid {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the seed feature's centroid as the reference point, false to not

Remarks

If this property is set to false, then you must specify [ITablePatternFeatureData::ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.md).

Example

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)
