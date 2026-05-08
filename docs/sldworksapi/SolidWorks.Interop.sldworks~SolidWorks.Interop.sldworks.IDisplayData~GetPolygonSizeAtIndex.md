# GetPolygonSizeAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex`

Gets the number of array elements returned by IDisplayData::GetPolygonAtIndex and IDisplayData::IGetPolygonAtIndex.
Gets the number of array elements returned by [IDisplayData::GetPolygonAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonAtIndex.md) and [IDisplayData::IGetPolygonAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolygonAtIndex.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPolygonSizeAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetPolygonSizeAtIndex(Index)
```

```

System.int GetPolygonSizeAtIndex( 
   System.int Index
)
```

```

System.int GetPolygonSizeAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index for the polygon

#### Return Value

Number of array elements returned by [IDisplayData::GetPolygonAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonAtIndex.md) and [IDisplayData::IGetPolygonAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolygonAtIndex.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetPolygonCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonCount.md)
