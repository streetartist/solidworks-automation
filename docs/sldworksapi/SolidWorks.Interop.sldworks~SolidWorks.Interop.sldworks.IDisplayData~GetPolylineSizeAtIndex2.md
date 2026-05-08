# GetPolylineSizeAtIndex2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolylineSizeAtIndex2`

Gets the number of array elements returned by IDisplayData::GetPolylineAtIndex2 and IDisplayData::IGetPolylineAtIndex2.
Gets the number of array elements returned by [IDisplayData::GetPolylineAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolylineAtIndex2.md) and [IDisplayData::IGetPolylineAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolylineAtIndex2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPolylineSizeAtIndex2( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetPolylineSizeAtIndex2(Index)
```

```

System.int GetPolylineSizeAtIndex2( 
   System.int Index
)
```

```

System.int GetPolylineSizeAtIndex2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired polyline where the index begins at zero

#### Return Value

Number array elements returned by [IDisplayData::GetPolylineAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolylineAtIndex2.md) and [IDisplayData::IGetPolylineAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolylineAtIndex2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::GetPolyLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolyLineCount.md)
