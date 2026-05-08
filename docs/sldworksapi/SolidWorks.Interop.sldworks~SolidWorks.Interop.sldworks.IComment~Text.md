# Text Property (IComment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Text`

Gets or sets the text for the comment.
Gets or sets the text for the comment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Text As System.String
```

```

Dim instance As IComment
Dim value As System.String
 
instance.Text = value
 
value = instance.Text
```

```

System.string Text {get; set;}
```

```

property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Text for the comment

Example

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)  
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)  
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md)  
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.md)
