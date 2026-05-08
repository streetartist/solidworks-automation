# SetTopLevelTransparency Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTopLevelTransparency`

Sets the transparency of this part or top-level assembly.
Sets the transparency of this part or top-level assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTopLevelTransparency( _
   ByVal InValue As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim InValue As System.Boolean
Dim value As System.Boolean
 
value = instance.SetTopLevelTransparency(InValue)
```

```

System.bool SetTopLevelTransparency( 
   System.bool InValue
)
```

```

System.bool SetTopLevelTransparency( 
   System.bool InValue
) 
```

#### Parameters

*InValue*
:   True to make this part or top-level assembly transparent, false to not

#### Return Value

True if transparency of this part or top-level assembly successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
