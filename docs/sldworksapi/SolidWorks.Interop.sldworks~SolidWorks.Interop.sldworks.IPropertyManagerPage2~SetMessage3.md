# SetMessage3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetMessage3`

Sets the message in this PropertyManager page.
Sets the message in this PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMessage3( _
   ByVal Message As System.String, _
   ByVal Visibility As System.Integer, _
   ByVal Expanded As System.Integer, _
   ByVal Caption As System.String _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPage2
Dim Message As System.String
Dim Visibility As System.Integer
Dim Expanded As System.Integer
Dim Caption As System.String
Dim value As System.Boolean
 
value = instance.SetMessage3(Message, Visibility, Expanded, Caption)
```

```

System.bool SetMessage3( 
   System.string Message,
   System.int Visibility,
   System.int Expanded,
   System.string Caption
)
```

```

System.bool SetMessage3( 
   System.String^ Message,
   System.int Visibility,
   System.int Expanded,
   System.String^ Caption
) 
```

#### Parameters

*Message*
:   Message text

*Visibility*
:   Visibility state of this message as defined by [swPropertyManagerPageMessageVisibility](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageMessageVisibility.html)

*Expanded*
:   Expand, compress, or leave the state of the message as is, as defined by [swPropertyManagerPageMessageExpanded](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageMessageExpanded.html)

*Caption*
:   Caption for message

#### Return Value

True if the message is set, false if not

Remarks

If Caption is empty, then the current caption is not changed.

This method should be useful when creating multi-page PropertyManager pages where you want different informational messages on each page.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)
