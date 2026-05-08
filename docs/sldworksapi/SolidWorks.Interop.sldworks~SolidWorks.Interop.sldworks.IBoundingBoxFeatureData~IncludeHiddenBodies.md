# IncludeHiddenBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~IncludeHiddenBodies`

Gets or sets whether to include hidden bodies in this bounding box feature.
Gets or sets whether to include hidden bodies in this bounding box feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeHiddenBodies As System.Boolean
```

```

Dim instance As IBoundingBoxFeatureData
Dim value As System.Boolean
 
instance.IncludeHiddenBodies = value
 
value = instance.IncludeHiddenBodies
```

```

System.bool IncludeHiddenBodies {get; set;}
```

```

property System.bool IncludeHiddenBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to include hidden bodies, false to not

Example

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.md)  
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.md)
