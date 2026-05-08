# BendEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~BendEdges`

Gets or sets the bend edges and faces in this convert solid feature.
Gets or sets the bend edges and faces in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendEdges As System.Object
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Object
 
instance.BendEdges = value
 
value = instance.BendEdges
```

```

System.object BendEdges {get; set;}
```

```

property System.Object^ BendEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of bend [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)s

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)
