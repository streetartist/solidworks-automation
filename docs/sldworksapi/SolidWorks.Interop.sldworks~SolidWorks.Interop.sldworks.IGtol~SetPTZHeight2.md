# SetPTZHeight2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight2`

Sets the projected tolerance zone for the specified frame and tolerance in this GTol.
Sets the projected tolerance zone for the specified frame and tolerance in this GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPTZHeight2( _
   ByVal FrameNumber As System.Integer, _
   ByVal TolNumber As System.Integer, _
   ByVal PtzDisplay As System.Boolean, _
   ByVal PtzHt As System.String _
) As System.Boolean
```

```

Dim instance As IGtol
Dim FrameNumber As System.Integer
Dim TolNumber As System.Integer
Dim PtzDisplay As System.Boolean
Dim PtzHt As System.String
Dim value As System.Boolean
 
value = instance.SetPTZHeight2(FrameNumber, TolNumber, PtzDisplay, PtzHt)
```

```

System.bool SetPTZHeight2( 
   System.int FrameNumber,
   System.int TolNumber,
   System.bool PtzDisplay,
   System.string PtzHt
)
```

```

System.bool SetPTZHeight2( 
   System.int FrameNumber,
   System.int TolNumber,
   System.bool PtzDisplay,
   System.String^ PtzHt
) 
```

#### Parameters

*FrameNumber*
:   Frame number

*TolNumber*
:   Tolerance number

*PtzDisplay*
:   True to display the projected zone tolerance, false to not

*PtzHt*
:   Height of the projected tolerance zone

#### Return Value

True if this method executed successfully, false if not

Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

The projected tolerance zone (PTZ) displays in the first tolerance window of the first control frame of the GTol. If PtzHt is not empty, its value is displayed after the PTZ symbol, which is a P enclosed in a circle.

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
[IGtol::GetPTZHeight2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2.md)
