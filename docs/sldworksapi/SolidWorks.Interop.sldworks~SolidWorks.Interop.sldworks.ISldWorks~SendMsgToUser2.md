# SendMsgToUser2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SendMsgToUser2`

Displays a message box containing a message to the user, who is required to interact with it before continuing.
Displays a message box containing a message to the user, who is required to interact with it before continuing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SendMsgToUser2( _
   ByVal Message As System.String, _
   ByVal Icon As System.Integer, _
   ByVal Buttons As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Message As System.String
Dim Icon As System.Integer
Dim Buttons As System.Integer
Dim value As System.Integer
 
value = instance.SendMsgToUser2(Message, Icon, Buttons)
```

```

System.int SendMsgToUser2( 
   System.string Message,
   System.int Icon,
   System.int Buttons
)
```

```

System.int SendMsgToUser2( 
   System.String^ Message,
   System.int Icon,
   System.int Buttons
) 
```

#### Parameters

*Message*
:   Message for user

*Icon*
:   Icon to show in the message box as defined in [swMessageBoxIcon\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxIcon_e.html)

*Buttons*
:   Buttons to show in the message box as defined in [swMessageBoxBtn\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxBtn_e.html)

#### Return Value

Value corresponding to the button the user clicked as defined in [swMessageBoxResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxResult_e.html)

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Detecting In-context Edit (C++)](Get_Edit_In_Context_Example_CPlusPlus_COM.htm)  
[Access Selections (VBA)](Access_Selections_Example_VB.htm)  
[Save Drawing As DXF (VBA)](Save_Drawing_as_DXF_Example_VB.htm)  
[Save Drawing as DXF (VB.NET)](Save_Drawing_as_DXF_Example_VBNET.htm)  
[Save Drawing as DXF (C#)](Save_Drawing_as_DXF_Example_CSharp.htm)  
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
