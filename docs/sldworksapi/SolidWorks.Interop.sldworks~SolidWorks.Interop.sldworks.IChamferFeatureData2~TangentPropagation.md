# TangentPropagation Property (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~TangentPropagation`

Gets or sets whether to extend the chamfer to all faces that are tangent to the selected faces or edges.
Gets or sets whether to extend the chamfer to all faces that are tangent to the selected faces or edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TangentPropagation As System.Boolean
```

```

Dim instance As IChamferFeatureData2
Dim value As System.Boolean
 
instance.TangentPropagation = value
 
value = instance.TangentPropagation
```

```

System.bool TangentPropagation {get; set;}
```

```

property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate chamfer to tangent faces, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)
