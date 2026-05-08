# GetBendLineCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount`

Gets the number of bendlines in a flat-pattern drawing view.
Gets the number of bendlines in a [flat-pattern drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsFlatPatternView.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBendLineCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetBendLineCount()
```

```

System.int GetBendLineCount()
```

```

System.int GetBendLineCount(); 
```

#### Return Value

Number of bendlines in a flat-pattern drawing view

Example

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)  
[Get Tangent Edges of Bendlines (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)  
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.md)  
[IView::IGetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.md)
