# SurfaceBodiesCount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~SurfaceBodiesCount`

Gets the number of surface bodies in a part document.
Gets the number of surface bodies in a part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property SurfaceBodiesCount As System.Integer
```

```

Dim instance As IFeatureStatistics
Dim value As System.Integer
 
value = instance.SurfaceBodiesCount
```

```

System.int SurfaceBodiesCount {get;}
```

```

property System.int SurfaceBodiesCount {
   System.int get();
}
```

#### Property Value

Number of surface bodies

Example

[Get Part's Feature Statistics (VB.NET)](Get_Part's_Feature_Statistics_Example_VBNET.htm)  
[Get Part's Feature Statistics (VBA)](Get_Part's_Feature_Statistics_Example_VB.htm)  
[Get Part's Feature Statistics (C#)](Get_Part's_Feature_Statistics_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureStatistics Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics.md)  
[IFeatureStatistics Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.md)  
[IFeatureStatistics::SolidBodiesCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~SolidBodiesCount.md)
