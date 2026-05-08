# InsertTitleBlockTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertTitleBlockTable`

Inserts a title block table in a part or assembly document.
Inserts a title block table in a part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertTitleBlockTable( _
   ByVal TemplateName As System.String, _
   ByVal X As System.Integer, _
   ByVal Y As System.Integer _
) As TitleBlockTableAnnotation
```

```

Dim instance As IModelDocExtension
Dim TemplateName As System.String
Dim X As System.Integer
Dim Y As System.Integer
Dim value As TitleBlockTableAnnotation
 
value = instance.InsertTitleBlockTable(TemplateName, X, Y)
```

```

TitleBlockTableAnnotation InsertTitleBlockTable( 
   System.string TemplateName,
   System.int X,
   System.int Y
)
```

```

TitleBlockTableAnnotation^ InsertTitleBlockTable( 
   System.String^ TemplateName,
   System.int X,
   System.int Y
) 
```

#### Parameters

*TemplateName*
:   Fully qualified path and name of the title block table template

*X*
:   x coordinate for upper-left corner of title block table

*Y*
:   y coordinate for upper-left corner of title block table

#### Return Value

[Title block table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableAnnotation.md)

Remarks

Title block table templates have a filename extension of .sldtbt.

Example

[Get Title Block Tables (VBA)](Get_Title_Block_Tables_Example_VB6.htm)  
[Get Title Block Tables (VB.NET)](Get_Title_Block_Tables_Example_VBNET.htm)  
[Get Title Block Tables (C#)](Get_Title_Block_Tables_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::InsertGeneralTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.md)
