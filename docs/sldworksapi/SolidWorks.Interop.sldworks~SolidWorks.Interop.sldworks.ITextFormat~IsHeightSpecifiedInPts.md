# IsHeightSpecifiedInPts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~IsHeightSpecifiedInPts`

Gets whether the character height is in points or system units.
Gets whether the character height is in points or system units.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsHeightSpecifiedInPts() As System.Boolean
```

```

Dim instance As ITextFormat
Dim value As System.Boolean
 
value = instance.IsHeightSpecifiedInPts()
```

```

System.bool IsHeightSpecifiedInPts()
```

```

System.bool IsHeightSpecifiedInPts(); 
```

#### Return Value

True if the character height is in points, false if it is in system units

Remarks

|  |  |
| --- | --- |
| **If the font height was set using...** | **Then this method returns...** |
| [ITextFormat::CharHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeight.md) | False |
| [ITextFormat::CharHeightInPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~CharHeightInPts.md) | True |

Example

[Get All Elements in Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)  
[Get Note Text Formatting Properties (VBA)](Get_Note_Text_Formatting_Properties_Example_VB.htm)  
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)  
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)  
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)  
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.md)
