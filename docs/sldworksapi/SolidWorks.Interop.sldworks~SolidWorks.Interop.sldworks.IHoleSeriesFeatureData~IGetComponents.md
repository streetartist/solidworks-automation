# IGetComponents Method (IHoleSeriesFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetComponents`

Obsolete. Superseded by IHoleSeriesFeatureData2::IGetComponents.
Obsolete. Superseded by [IHoleSeriesFeatureData2::IGetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetComponents.md).

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

Dim instance As IHoleSeriesFeatureData
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

Before calling this method, call [IHoleSeriesFeatureData::GetComponentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponentsCount.md) to get the value for NCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.md)  
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.md)  
[IHoleSeriesFeatureData::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponents.md)
