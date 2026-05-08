# GetPenInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetPenInfo`

Gets information about the pens used in SOLIDWORKS.
Gets information about the pens used in SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPenInfo() As System.Object
```

```

Dim instance As IDrawingDoc
Dim value As System.Object
 
value = instance.GetPenInfo()
```

```

System.object GetPenInfo()
```

```

System.Object^ GetPenInfo(); 
```

#### Return Value

Array containing an array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm) and see **Remarks**)

Remarks

The return value is the following array: **[** *font, weight, color* **]**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetPenInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetPenInfo.md)  
[IDrawingDoc::IGetPenInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetPenInfo.md)
