# CenterLineFont Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~CenterLineFont`

Gets or sets whether the centerline font is used for the lines in this center mark.
Gets or sets whether the centerline font is used for the lines in this center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CenterLineFont As System.Boolean
```

```

Dim instance As ICenterMark
Dim value As System.Boolean
 
instance.CenterLineFont = value
 
value = instance.CenterLineFont
```

```

System.bool CenterLineFont {get; set;}
```

```

property System.bool CenterLineFont {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if centerline font is used for the lines in center marks, false if not

Example

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)
