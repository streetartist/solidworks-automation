# Bold Property (IPropertyManagerPageLabel)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Bold`

Gets or sets whether the range of specified characters are bolded in this ProperytManager label.
Gets or sets whether the range of specified characters are bolded in this ProperytManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Bold( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Boolean
 
instance.Bold(StartChar, EndChar) = value
 
value = instance.Bold(StartChar, EndChar)
```

```

System.bool Bold( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.bool Bold {
   System.bool get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.bool value);
}
```

#### Parameters

*StartChar*
:   0-based index value of start character

*EndChar*
:   0-based index value of end character

#### Property Value

TRUE to bold the specified range of characters, FALSE to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
