# ResetUntitledCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ResetUntitledCount`

Resets the index of untitled documents.
Resets the index of untitled documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ResetUntitledCount( _
   ByVal PartValue As System.Integer, _
   ByVal AssemValue As System.Integer, _
   ByVal DrawingValue As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim PartValue As System.Integer
Dim AssemValue As System.Integer
Dim DrawingValue As System.Integer
Dim value As System.Integer
 
value = instance.ResetUntitledCount(PartValue, AssemValue, DrawingValue)
```

```

System.int ResetUntitledCount( 
   System.int PartValue,
   System.int AssemValue,
   System.int DrawingValue
)
```

```

System.int ResetUntitledCount( 
   System.int PartValue,
   System.int AssemValue,
   System.int DrawingValue
) 
```

#### Parameters

*PartValue*
:   Starting index for part documents

*AssemValue*
:   Starting index for assembly documents

*DrawingValue*
:   Starting index for drawing documents

#### Return Value

Total number of successful resets

Remarks

Use this method to reset untitled document indexes so that playbacks of the macro recorder increment untitled documents in a reproducible fashion.

For example, if the first playback of a macro creates Part1 and Part2, then the second playback may fail because it creates Part3 and Part4 instead of Part1 and Part2.

To ensure reproducible results, call ISldWorks::ResetUntitledCount at the beginning or end of a macro program.

Example

[Reset Untitled Document Count (VBA)](Reset_Untitled_Document_Count_Example_VB.htm)  
[Reset Untitled Document Count (VB.NET)](Reset_Untitled_Document_Count_Example_VBNET.htm)  
[Reset Untitled Document Count (C#)](Reset_Untitled_Document_Count_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
