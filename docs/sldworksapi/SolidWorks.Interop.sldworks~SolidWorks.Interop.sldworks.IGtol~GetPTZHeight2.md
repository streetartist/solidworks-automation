# GetPTZHeight2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2`

Gets the projected tolerance zone for the specified frame and tolerance in this GTol.
Gets the projected tolerance zone for the specified frame and tolerance in this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPTZHeight2( _
   ByVal FrameNumber As System.Integer, _
   ByVal TolNumber As System.Integer, _
   ByRef PtzDisplay As System.Boolean, _
   ByRef PtzHt As System.String _
) As System.Boolean
```

```

Dim instance As IGtol
Dim FrameNumber As System.Integer
Dim TolNumber As System.Integer
Dim PtzDisplay As System.Boolean
Dim PtzHt As System.String
Dim value As System.Boolean
 
value = instance.GetPTZHeight2(FrameNumber, TolNumber, PtzDisplay, PtzHt)
```

```

System.bool GetPTZHeight2( 
   System.int FrameNumber,
   System.int TolNumber,
   out System.bool PtzDisplay,
   out System.string PtzHt
)
```

```

System.bool GetPTZHeight2( 
   System.int FrameNumber,
   System.int TolNumber,
   [Out] System.bool PtzDisplay,
   [Out] System.String^ PtzHt
) 
```

#### Parameters

*FrameNumber*
:   Frame number

*TolNumber*
:   Tolerance number

*PtzDisplay*
:   True if the projected zone tolerance is displayed in the GTol, false if not

*PtzHt*
:   Height of the projected tolerance zone

#### Return Value

True if the method executed successfully, false if not

Remarks

This method:

- is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.
- returns the height of the projected tolerance zone as a string because it is a user-specified parameter that can be textual, numeric, or both types of data.

Example

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)  
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)  
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::SetPTZHeight2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight2.md)
