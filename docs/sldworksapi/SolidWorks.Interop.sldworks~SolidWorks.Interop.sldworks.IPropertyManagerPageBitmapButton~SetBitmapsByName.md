# SetBitmapsByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsByName`

Obsolete. Superseded by IPropertyManagerPageBitmapButton::SetBitmapsByName2.
Obsolete. Superseded by [IPropertyManagerPageBitmapButton::SetBitmapsByName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsByName2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBitmapsByName( _
   ByVal BitmapUp As System.String, _
   ByVal BitmapDown As System.String, _
   ByVal BitmapDisabled As System.String _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageBitmapButton
Dim BitmapUp As System.String
Dim BitmapDown As System.String
Dim BitmapDisabled As System.String
Dim value As System.Boolean
 
value = instance.SetBitmapsByName(BitmapUp, BitmapDown, BitmapDisabled)
```

```

System.bool SetBitmapsByName( 
   System.string BitmapUp,
   System.string BitmapDown,
   System.string BitmapDisabled
)
```

```

System.bool SetBitmapsByName( 
   System.String^ BitmapUp,
   System.String^ BitmapDown,
   System.String^ BitmapDisabled
) 
```

#### Parameters

*BitmapUp*

*BitmapDown*

*BitmapDisabled*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.md)  
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.md)
