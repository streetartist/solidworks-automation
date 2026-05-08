# IsBendLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IsBendLine`

Gets whether the sketch segment is a bendline.
Gets whether the sketch segment is a bendline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsBendLine() As System.Boolean
```

```

Dim instance As ISketchSegment
Dim value As System.Boolean
 
value = instance.IsBendLine()
```

```

System.bool IsBendLine()
```

```

System.bool IsBendLine(); 
```

#### Return Value

True if the sketch segment is a bendline, false if not

Example

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)  
[Get Tangent Edges of Bendlines (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)  
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[IView::GetBendLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount.md)  
[IView::GetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.md)  
[IView::IGetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.md)
