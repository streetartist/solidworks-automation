# GetLines Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLines`

Gets all of the lines in the current sketch.
Gets all of the lines in the current sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLines() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.GetLines()
```

```

System.object GetLines()
```

```

System.Object^ GetLines(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

[ LineType, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ... ]

where this array of 7 values repeats itself for each line in the current sketch. The number of doubles returned is (lineCount \* 7). To determine the number of lines in the current sketch, use [IModelDoc2::GetLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLineCount.md).

See [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) for valid line types.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IGetLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetLines.md)  
[IModelDoc2::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLineCount.md)
