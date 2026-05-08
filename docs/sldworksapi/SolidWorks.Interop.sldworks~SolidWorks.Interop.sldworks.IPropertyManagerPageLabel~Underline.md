# Underline Property (IPropertyManagerPageLabel)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Underline`

Gets or sets whether to apply the specified underline style to the specified range of characters in this PropertyManager label.
Gets or sets whether to apply the specified underline style to the specified range of characters in this PropertyManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Underline( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Integer
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Integer
 
instance.Underline(StartChar, EndChar) = value
 
value = instance.Underline(StartChar, EndChar)
```

```

System.int Underline( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.int Underline {
   System.int get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.int value);
}
```

#### Parameters

*StartChar*
:   0-based index value of start character

*EndChar*
:   0-based index value of end character

#### Property Value

Underline style as defined in [swPropMgrPageLabelUnderlineStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageLabelUnderlineStyle_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
