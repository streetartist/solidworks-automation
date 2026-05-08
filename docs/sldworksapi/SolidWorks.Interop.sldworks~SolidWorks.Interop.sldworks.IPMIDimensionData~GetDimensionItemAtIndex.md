# GetDimensionItemAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~GetDimensionItemAtIndex`

Gets the PMI dimension item at the specified index.
Gets the PMI dimension item at the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDimensionItemAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IPMIDimensionData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetDimensionItemAtIndex(Index)
```

```

System.object GetDimensionItemAtIndex( 
   System.int Index
)
```

```

System.Object^ GetDimensionItemAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Zero-based index of the dimension item to get

#### Return Value

[IPMIDimensionItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.md)

Remarks

Use [IPMIDimensionData::GetDimensionItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~GetDimensionItemCount.md) to set Index.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDimensionData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.md)  
[IPMIDimensionData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.md)
