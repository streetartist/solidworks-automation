# SlicesToGenerate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~SlicesToGenerate`

Gets or sets the slicing method.
Gets or sets the slicing method.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SlicesToGenerate As System.Integer
```

```

Dim instance As ISlicingData
Dim value As System.Integer
 
instance.SlicesToGenerate = value
 
value = instance.SlicesToGenerate
```

```

System.int SlicesToGenerate {get; set;}
```

```

property System.int SlicesToGenerate {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Slicing method as defined in [swSlicingTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlicingTypes_e.html)

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)
