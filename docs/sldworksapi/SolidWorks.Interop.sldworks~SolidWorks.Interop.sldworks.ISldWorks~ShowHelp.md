# ShowHelp Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowHelp`

Displays the specified Help topic.
Displays the specified Help topic.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowHelp( _
   ByVal HelpFile As System.String, _
   ByVal HelpTopic As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim HelpFile As System.String
Dim HelpTopic As System.Integer
 
instance.ShowHelp(HelpFile, HelpTopic)
```

```

void ShowHelp( 
   System.string HelpFile,
   System.int HelpTopic
)
```

```

void ShowHelp( 
   System.String^ HelpFile,
   System.int HelpTopic
) 
```

#### Parameters

*HelpFile*
:   Name of the Help file that contains the Help topic

*HelpTopic*
:   ID of Help topic to display

Remarks

You can use this method with [ISldWorks::AddCallback](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.md) to implement Interactive What's New for your add-in.

Example

STDMETHODIMP CFuncFeatApp::appCallbackFunction(int cmd,int data,LPDISPATCH dsp, BOOL \*retval)

{

            switch (cmd)

            {

            case     swAppIsNewCmd:

                        \*retval = VARIANT\_True; //Set to True if data is new

                        break;

            case     swAppWhatsNewDescription:

                            m\_iSldWorks->ShowHelp(\_T("name\_of\_your\_Help\_system.chm"), cmd);

                        break;

            case     swAppHelpContext:

                        break;

            }

            return S\_OK;

}

Example

[Call Compiled HTML Help File (C#)](Call_Compiled_HTML_Help_File_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CallBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.md)  
[ISldWorks::RemoveCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.md)  
[ISldWorks::SetAddinCallbackInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo.md)
