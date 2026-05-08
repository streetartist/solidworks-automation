# AddCommandItem Method (ICommandGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem`

Obsolete. Superseded by ICommandGroup::AddComandItem2.
Obsolete. Superseded by [ICommandGroup::AddComandItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCommandItem( _
   ByVal Name As System.String, _
   ByVal Position As System.Integer, _
   ByVal HintString As System.String, _
   ByVal ToolTip As System.String, _
   ByVal ImageListIndex As System.Integer, _
   ByVal CallbackFunction As System.String, _
   ByVal EnableMethod As System.String, _
   ByVal UserID As System.Integer _
) As System.Integer
```

```

Dim instance As ICommandGroup
Dim Name As System.String
Dim Position As System.Integer
Dim HintString As System.String
Dim ToolTip As System.String
Dim ImageListIndex As System.Integer
Dim CallbackFunction As System.String
Dim EnableMethod As System.String
Dim UserID As System.Integer
Dim value As System.Integer
 
value = instance.AddCommandItem(Name, Position, HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, UserID)
```

```

System.int AddCommandItem( 
   System.string Name,
   System.int Position,
   System.string HintString,
   System.string ToolTip,
   System.int ImageListIndex,
   System.string CallbackFunction,
   System.string EnableMethod,
   System.int UserID
)
```

```

System.int AddCommandItem( 
   System.String^ Name,
   System.int Position,
   System.String^ HintString,
   System.String^ ToolTip,
   System.int ImageListIndex,
   System.String^ CallbackFunction,
   System.String^ EnableMethod,
   System.int UserID
) 
```

#### Parameters

*Name*

*Position*

*HintString*

*ToolTip*

*ImageListIndex*

*CallbackFunction*

*EnableMethod*

*UserID*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)
