# GetFromToListHeaderDefinitions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~GetFromToListHeaderDefinitions`

Gets the headers from a routing from-to list.
Gets the headers from a routing from-to list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFromToListHeaderDefinitions( _
   ByRef WireNameHdr As System.String, _
   ByRef FromRefHdr As System.String, _
   ByRef FromPinHdr As System.String, _
   ByRef FromPartnoHdr As System.String, _
   ByRef ToRefHdr As System.String, _
   ByRef ToPinHdr As System.String, _
   ByRef ToPartnoHdr As System.String, _
   ByRef CableNameHdr As System.String, _
   ByRef CoreNameHdr As System.String, _
   ByRef ColourHdr As System.String, _
   ByRef WireSpecHdr As System.String, _
   ByRef OtherAttribHdr As System.String _
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
 
value = instance.GetFromToListHeaderDefinitions(WireNameHdr, FromRefHdr, FromPinHdr, FromPartnoHdr, ToRefHdr, ToPinHdr, ToPartnoHdr, CableNameHdr, CoreNameHdr, ColourHdr, WireSpecHdr, OtherAttribHdr)
```

```

System.bool GetFromToListHeaderDefinitions( 
   out System.string WireNameHdr,
   out System.string FromRefHdr,
   out System.string FromPinHdr,
   out System.string FromPartnoHdr,
   out System.string ToRefHdr,
   out System.string ToPinHdr,
   out System.string ToPartnoHdr,
   out System.string CableNameHdr,
   out System.string CoreNameHdr,
   out System.string ColourHdr,
   out System.string WireSpecHdr,
   out System.string OtherAttribHdr
)
```

```

System.bool GetFromToListHeaderDefinitions( 
   [Out] System.String^ WireNameHdr,
   [Out] System.String^ FromRefHdr,
   [Out] System.String^ FromPinHdr,
   [Out] System.String^ FromPartnoHdr,
   [Out] System.String^ ToRefHdr,
   [Out] System.String^ ToPinHdr,
   [Out] System.String^ ToPartnoHdr,
   [Out] System.String^ CableNameHdr,
   [Out] System.String^ CoreNameHdr,
   [Out] System.String^ ColourHdr,
   [Out] System.String^ WireSpecHdr,
   [Out] System.String^ OtherAttribHdr
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

Example

See the [IRoutingSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRoutingSettings Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings.md)  
[IRoutingSettings Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.md)  
[IRoutingSettings::SetFromToListHeaderDefinitions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings~SetFromToListHeaderDefinitions.md)
