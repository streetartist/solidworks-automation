# GetBodiesToCombineCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~GetBodiesToCombineCount`

Gets the number of bodies to combine.
Gets the number of bodies to combine.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodiesToCombineCount() As System.Integer
```

```

Dim instance As ICombineBodiesFeatureData
Dim value As System.Integer
 
value = instance.GetBodiesToCombineCount()
```

```

System.int GetBodiesToCombineCount()
```

```

System.int GetBodiesToCombineCount(); 
```

#### Return Value

Number of bodies to combine

Remarks

Call this method before calling [ICombineBodiesFeatureData::IGetBodiesToCombine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.md)  
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.md)  
[IColorTable::ISetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ISetBodiesToCombine.md)  
[IColorTable::BodiesToCombine Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.md)
