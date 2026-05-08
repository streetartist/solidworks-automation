# GetTextFormatItems Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetTextFormatItems`

Gets the format tokens of the specified text portion of a multi-value display dimension.
Gets the format tokens of the specified text portion of a multi-value display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextFormatItems( _
   ByVal WhichText As System.Integer, _
   ByRef TokensDefinition As System.Object, _
   ByRef TokensEvaluated As System.Object _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim WhichText As System.Integer
Dim TokensDefinition As System.Object
Dim TokensEvaluated As System.Object
Dim value As System.Integer
 
value = instance.GetTextFormatItems(WhichText, TokensDefinition, TokensEvaluated)
```

```

System.int GetTextFormatItems( 
   System.int WhichText,
   out System.object TokensDefinition,
   out System.object TokensEvaluated
)
```

```

System.int GetTextFormatItems( 
   System.int WhichText,
   [Out] System.Object^ TokensDefinition,
   [Out] System.Object^ TokensEvaluated
) 
```

#### Parameters

*WhichText*
:   Portion of the display dimension text as defined in [swDimensionTextParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionTextParts_e.html)

*TokensDefinition*
:   Array of strings containing format symbols for the text portion specified in WhichText

*TokensEvaluated*
:   Array of strings containing evaluations of symbols in TokensDefinition

#### Return Value

Size of returned arrays

Remarks

Each display dimension's PropertyManager page contains a section called Dimension Text that specifies the format of the displayed dimension. The format consists of function symbols or tokens enclosed within angle brackets (e.g., <DIM>), each of which connotes the function or definition of the value symbols that follow it.

This method retrieves all of the symbols, both function and value, for the portion of the display dimension text specified by WhichText. It also retrieves values for any symbols that can be evaluated in TokensDefinition.

**NOTE:** This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md).

Example

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)  
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)  
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.md)
