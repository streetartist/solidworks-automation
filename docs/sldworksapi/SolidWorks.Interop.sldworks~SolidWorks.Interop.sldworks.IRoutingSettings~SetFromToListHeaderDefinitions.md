# SetFromToListHeaderDefinitions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetFromToListHeaderDefinitions`

Sets the headers in a routing from-to list.
Sets the headers in a routing from-to list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFromToListHeaderDefinitions( _
   ByVal WireNameHdr As System.String, _
   ByVal FromRefHdr As System.String, _
   ByVal FromPinHdr As System.String, _
   ByVal FromPartnoHdr As System.String, _
   ByVal ToRefHdr As System.String, _
   ByVal ToPinHdr As System.String, _
   ByVal ToPartnoHdr As System.String, _
   ByVal CableNameHdr As System.String, _
   ByVal CoreNameHdr As System.String, _
   ByVal ColourHdr As System.String, _
   ByVal WireSpecHdr As System.String, _
   ByVal OtherAttribHdr As System.String _
) As System.Boolean
```

```

Dim instance As IRoutingSettings
Dim WireNameHdr As System.String
Dim FromRefHdr As System.String
Dim FromPinHdr As System.String
Dim FromPartnoHdr As System.String
Dim ToRefHdr As System.String
Dim ToPinHdr As System.String
Dim ToPartnoHdr As System.String
Dim CableNameHdr As System.String
Dim CoreNameHdr As System.String
Dim ColourHdr As System.String
Dim WireSpecHdr As System.String
Dim OtherAttribHdr As System.String
Dim value As System.Boolean
 
value = instance.SetFromToListHeaderDefinitions(WireNameHdr, FromRefHdr, FromPinHdr, FromPartnoHdr, ToRefHdr, ToPinHdr, ToPartnoHdr, CableNameHdr, CoreNameHdr, ColourHdr, WireSpecHdr, OtherAttribHdr)
```

```

System.bool SetFromToListHeaderDefinitions( 
   System.string WireNameHdr,
   System.string FromRefHdr,
   System.string FromPinHdr,
   System.string FromPartnoHdr,
   System.string ToRefHdr,
   System.string ToPinHdr,
   System.string ToPartnoHdr,
   System.string CableNameHdr,
   System.string CoreNameHdr,
   System.string ColourHdr,
   System.string WireSpecHdr,
   System.string OtherAttribHdr
)
```

```

System.bool SetFromToListHeaderDefinitions( 
   System.String^ WireNameHdr,
   System.String^ FromRefHdr,
   System.String^ FromPinHdr,
   System.String^ FromPartnoHdr,
   System.String^ ToRefHdr,
   System.String^ ToPinHdr,
   System.String^ ToPartnoHdr,
   System.String^ CableNameHdr,
   System.String^ CoreNameHdr,
   System.String^ ColourHdr,
   System.String^ WireSpecHdr,
   System.String^ OtherAttribHdr
) 
```

#### Parameters

*WireNameHdr*
:   Wire name header

*FromRefHdr*
:   "From" reference header

*FromPinHdr*
:   "From" pin header

*FromPartnoHdr*
:   "From" part number header

*ToRefHdr*
:   "To" reference header

*ToPinHdr*
:   "To" pin header

*ToPartnoHdr*
:   "To" part number header

*CableNameHdr*
:   Cable name header

*CoreNameHdr*
:   Core name header

*ColourHdr*
:   Color header

*WireSpecHdr*
:   Wire specification header

*OtherAttribHdr*
:   Miscellaneous header

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::GetFromToListHeaderDefinitions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetFromToListHeaderDefinitions.md)
