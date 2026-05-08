# InsertGeneralToleranceTableAnnotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralToleranceTableAnnotation`

Inserts a general tolerance table annotation in this model document.
Inserts a general tolerance table annotation in this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertGeneralToleranceTableAnnotation( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer _
) As GeneralToleranceTableAnnotation
```

```

Dim instance As IModelDocExtension
Dim TemplateName As System.String
Dim X As System.Integer
Dim Y As System.Integer
Dim value As GeneralToleranceTableAnnotation
 
value = instance.InsertGeneralToleranceTableAnnotation(TemplateName, X, Y)
```

```

GeneralToleranceTableAnnotation InsertGeneralToleranceTableAnnotation( 
   System.string TemplateName,
   System.int X,
   System.int Y
)
```

```

GeneralToleranceTableAnnotation^ InsertGeneralToleranceTableAnnotation( 
   System.String^ TemplateName,
   System.int X,
   System.int Y
) 
```

#### Parameters

*TemplateName*
:   Path and file name of the table template to use (see **Remarks**)

*X*
:   X coordinate of this table annotation

*Y*
:   Y coordinate of this table annotation

#### Return Value

[IGeneralToleranceTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableAnnotation.md)

Remarks

Specify TemplateName with *install\_dir***\lang\***lang***\bom-standard.sldbomtbt**.

Example

[Insert General Tolerance Table (VBA)](Insert_General_Tolerance_Table_Example_VB.htm)  
[Insert General Tolerance Table (VB.NET)](Insert_General_Tolerance_Table_Example_VBNET.htm)  
[Insert General Tolerance Table (C#)](Insert_General_Tolerance_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IGeneralToleranceTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature.md)
