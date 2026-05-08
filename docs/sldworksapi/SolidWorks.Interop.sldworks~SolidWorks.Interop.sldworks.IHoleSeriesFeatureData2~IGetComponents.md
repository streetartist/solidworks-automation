# IGetComponents Method (IHoleSeriesFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetComponents`

Gets the components in this hole series.
Gets the components in this hole series.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetComponents( _
   ByVal NCount As System.Integer _
) As Component2
```

```

Dim instance As IHoleSeriesFeatureData2
Dim NCount As System.Integer
Dim value As Component2
 
value = instance.IGetComponents(NCount)
```

```

Component2 IGetComponents( 
   System.int NCount
)
```

```

Component2^ IGetComponents( 
   System.int NCount
) 
```

#### Parameters

*NCount*
:   Number of components in this hole series

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in this hole series

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IHoleSeriesFeatureData2::GetComponentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetComponentsCount.md) to get the value for NCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md)  
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.md)  
[IHoleSeriesFeatureData2::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetComponents.md)
